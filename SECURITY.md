# Security policy

## Supported branch

Only `main` is maintained. Releases are dated snapshots of `main` with the PDF books; they are
not patched, and fixes land in `main`.

## What counts as a security or privacy issue here

This repository is public interview content, not a running service, but please
report privately if you find:

- Personal data or private material that slipped into the repository or its
  git history (names, contact details, CVs, private paths, private chat links,
  or anything else that identifies a candidate).
- Secrets or credentials committed anywhere, including in old commits.
- NDA or confidential material presented as a source.
- A cited source link that has been hijacked or now points to something malicious.
- A vulnerability in `scripts/`, `.github/workflows/` or `.githooks/` that could
  run untrusted code or leak secrets during a build or check.

## How to report

Use GitHub's private vulnerability reporting:
<https://github.com/eiler2005/ai-interview-atlas/security/advisories/new>

Do not open a public issue that repeats the personal data or secret you
found — that would republish exactly what needs to be removed. If the link
above does not work, open a public issue titled "Private report" that contains
no details, and the maintainer will arrange a private channel.

## What happens next

- We acknowledge the report and confirm what is exposed and where.
- We remove the material from the current tree and, when it is in git
  history, rewrite history and force-push to purge it, then ask anyone with
  a clone to re-clone rather than pull.
- Where useful, we add a rule to the privacy checker
  (`.githooks/privacy-check`) or to CI so the same class of problem is
  caught automatically next time.
