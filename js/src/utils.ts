import { isObject } from '@rjsf/utils';
import { TDataSet, TUrlKey, ALL_KEYS, DEFAULTS } from './tokens';

export function getDataSet(el: HTMLElement): TDataSet {
  const dataset: TDataSet = {};
  for (const k of [...ALL_KEYS]) {
    dataset[k] = el.dataset[k] || DEFAULTS[k];
  }
  return dataset;
}

export async function getFileContent(
  dataset: TDataSet,
  formData: any,
): Promise<string> {
  const format = dataset.prjsfDataFormat;
  if (dataset.prjsfPruneEmpty === 'true') {
    formData = pruneObject(formData);
  }

  if (formData == null) {
    return '';
  }

  switch (format) {
    case 'json':
      return JSON.stringify(formData, null, 2);
    case 'toml':
      let toml = await import('smol-toml');
      return toml.stringify(formData);
    case 'yaml':
      let yaml = await import('yaml');
      return yaml.stringify(formData);
  }
  return '';
}

function pruneObject(data: Record<string, any>) {
  let newData: Record<string, any> = {};
  for (let [key, value] of Object.entries(data)) {
    if (Array.isArray(value) && !value.length) {
      continue;
    }

    if (isObject(value)) {
      value = pruneObject(value);
    }

    if (value == null) {
      continue;
    }
    newData[key] = value;
  }
  return [...Object.keys(newData)].length ? newData : null;
}

export async function fetchData(dataset: TDataSet, key: TUrlKey): Promise<any> {
  let url = dataset[key];

  if (!url) {
    return {};
  }

  const response = await fetch(url);
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

  return data;
}
