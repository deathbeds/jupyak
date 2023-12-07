import React from 'react';
import type { RJSFSchema } from '@rjsf/utils';
import type { FormProps, IChangeEvent } from '@rjsf/core';
import * as toml from 'smol-toml';
import validator from '@rjsf/validator-ajv8';
import { render } from 'react-dom';
import Form from '@rjsf/bootstrap-4';



async function main() {
  const params = new URLSearchParams(window.location.search);
  const schema = await getSchema(`${params.get('schema')}`);
  const formData = await getConfig(`${params.get('config')}`);
  renderForm(schema, formData);
}

async function onChange(data: IChangeEvent) {
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

async function renderForm(schema: RJSFSchema, formData: Record<string, any>) {
  const formProps: FormProps = {
    schema,
    validator,
    liveValidate: true,
    formData,
    onChange,
  };

  render(<Form {...formProps} />, document.getElementById('form'));
}

async function getSchema(path: string): Promise<RJSFSchema> {
  return await (await fetch(path)).json();
}

async function getConfig(path: string): Promise<Record<string, any>> {
  const configText = await (await fetch(path)).text();

  let formData = {};

  if (path.endsWith('.toml')) {
    const toml = await import('smol-toml');
    formData = toml.parse(configText);
  }

  return formData;
}

void main();
