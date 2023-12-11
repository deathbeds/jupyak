import type { FormProps } from '@rjsf/core';
import validator from '@rjsf/validator-ajv8';
import { Fragment, render } from 'react-dom';
import { useState } from 'react';
import Form from '@rjsf/bootstrap-4';

import { TDataSet } from './tokens';

import { fetchData, getFileContent, getDataSet } from './utils';

export async function makeOneForm(container: HTMLElement): Promise<void> {
  const dataset = getDataSet(container);

  const [schema, uiSchema, formData] = await Promise.all([
    fetchData(dataset, 'prjsfSchema'),
    fetchData(dataset, 'prjsfUiSchema'),
    fetchData(dataset, 'prjsfData'),
  ]);

  const form = formComponent(dataset, { schema, formData, uiSchema });
  render(form, container);
}

export function formComponent(dataset: TDataSet, props: Partial<FormProps>) {
  const PRJSF = () => {
    const [value, setValue] = useState('');
    const [url, setUrl] = useState('#');
    const [formData, setFormData] = useState(props.formData);
    const [fileName, setFileName] = useState(dataset.prjsfFileName || '');

    const updateUrl = () => {
      let url = new URL(dataset.prjsfGithubUrl || '#', window.location.href);
      url.searchParams.set('value', value);
      url.searchParams.set('fileName', fileName);
      setUrl(url.toString());
    };

    const updateFormData = async (formData: any) => {
      let value = await getFileContent(dataset, formData);
      setValue(value);
      setFormData(formData);
      updateUrl();
    };

    if (!value) {
      void updateFormData(formData);
    }

    const formProps: FormProps = {
      schema: {},
      validator,
      liveValidate: true,
      onChange: async ({ formData }) => await updateFormData(formData),
      ...props,
    };

    return (
      <div class="card prjsf">
        <ul class="list-group list-group-flush">
          <li class="list-group-item">
            <Form {...formProps} formData={formData}>
              <Fragment />
            </Form>
          </li>
          <li class="list-group-item">
            <label class="form-label">Preview</label>
            <textarea
              className="form-control"
              value={value}
              spellCheck={false}
              rows={10}
            ></textarea>
          </li>
          <li class="list-group-item">
            <label class="form-label">
              {dataset.prjsfDataFormat?.toUpperCase()} file name
            </label>
            <input
              type="text"
              className="form-control"
              placeholder={fileName}
              onChange={(change) => {
                setFileName(change.currentTarget.value);
                updateUrl();
              }}
            />
          </li>
          <li class="list-group-item">
            <a
              href={url}
              class="form-control btn btn-primary btn-lg"
              role="button"
              target="_blank"
            >
              Start Pull Request with <code>{fileName}</code>
            </a>
          </li>
        </ul>
      </div>
    );
  };

  return <PRJSF />;
}
