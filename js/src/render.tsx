import type { FormProps, IChangeEvent } from '@rjsf/core';
import validator from '@rjsf/validator-ajv8';
import { render } from 'react-dom';
import Form from '@rjsf/bootstrap-4';

import { TDataSet, ALL_KEYS, TUrlKey } from './tokens';

export async function makeOneForm(container: HTMLElement): Promise<void> {
  const dataset = getDataSet(container);

  const [schema, uiSchema, formData] = await Promise.all([
    fetchData(dataset, 'prjsfSchema'),
    fetchData(dataset, 'prjsfUiSchema'),
    fetchData(dataset, 'prjsfData'),
  ]);

  await renderForm(container, dataset, { schema, formData, uiSchema });
}

export function getDataSet(el: HTMLElement): TDataSet {
  const dataset: TDataSet = {};
  for (const k of [...ALL_KEYS]) {
    dataset[k] = el.dataset[k];
  }
  return dataset;
}

export async function renderForm(
  container: HTMLElement,
  dataset: TDataSet,
  props: Partial<FormProps>,
) {
  const formProps: FormProps = {
    schema: {},
    validator,
    liveValidate: true,
    onChange: makeOnChange(dataset),
    ...props,
  };

  render(<Form {...formProps} />, container);
}

function makeOnChange(dataset: TDataSet) {
  async function onChange(data: IChangeEvent) {
    let toml = await import('smol-toml');
    const tomlText = toml.stringify(data.formData);
    const url = new URL('https://github.com/deathbeds/jupyak/new/main');
    url.searchParams.set('filename', tomlText);

    const preview: HTMLTextAreaElement | null =
      document.querySelector('#submit textarea');

    if (preview) {
      preview.value = tomlText;
    }

    const link: HTMLAnchorElement | null = document.querySelector('#submit a');
    if (link) {
      link.setAttribute('href', url.toString());
    }
  }
  return onChange;
}

async function fetchData(dataset: TDataSet, key: TUrlKey): Promise<any> {
  let url = dataset[key];

  if (!url) {
    return {};
  }

  let response = await fetch(url);
  let data: any = null;
  const format = dataset[`${key}Format`] || 'json';
  if (response.ok) {
    switch (format) {
      case 'json':
        data = await response.json();
        break;
      case 'toml':
        let toml = await import('smol-toml');
        data = toml.parse(await response.text());
        break;
      case 'yaml':
        let yaml = await import('yaml');
        data = yaml.parse(await response.text());
        break;
    }
  }
  console.warn('data', data);
  return data;
}

// async function getConfig(path: string): Promise<Record<string, any>> {
//   const configText = await (await fetch(path)).text();

//   let formData = {};

//   if (path.endsWith('.toml')) {
//     const toml = await import('smol-toml');
//     formData = toml.parse(configText);
//   }

//   return formData;
// }
