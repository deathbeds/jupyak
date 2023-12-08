export const PROVIDER_KEYS = ['prjsfGithubUrl'] as const;
export const URL_KEYS = ['prjsfData', 'prjsfSchema', 'prjsfUiSchema'] as const;
export const FORMAT_KEYS = [
  'prjsfSchemaFormat',
  'prjsfUiSchemaFormat',
  'prjsfDataFormat',
] as const;
export const ALL_KEYS = [...PROVIDER_KEYS, ...URL_KEYS, ...FORMAT_KEYS];

export type TProviderKey = (typeof PROVIDER_KEYS)[number];
export type TFormatKey = (typeof FORMAT_KEYS)[number];
export type TUrlKey = (typeof URL_KEYS)[number];
export type TDataKey = TProviderKey | TFormatKey | TUrlKey;

export type TDataSet = Partial<{
  [K in TDataKey]: string | null;
}>;
