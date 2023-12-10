const SELECTOR = '[data-prjsf-github-url]';

export async function main() {
  const containers = [...document.querySelectorAll(SELECTOR)];

  if (!containers.length) {
    return;
  }

  const { makeOneForm } = await import('./render');

  containers.forEach(makeOneForm);
}
void main();
