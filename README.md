# Date Shift Guard

Browser-only GitHub Pages micro-tool for catching JavaScript `YYYY-MM-DD` off-by-one bugs before they ship.

Pain picked from public dev surfaces: a current Hacker News discussion about JavaScript `Date`, Temporal, and date-only strings noted that `new Date("2026-01-12")` can render as the previous day in local time zones. This tool makes that failure mode visible and gives safer snippets for date-only API fields.

## What it does

- Checks one `YYYY-MM-DD` value against common display time zones.
- Scans pasted JSON for date-only strings.
- Shows whether native JavaScript `Date` parsing shifts the displayed calendar day.
- Generates safe browser-side handling snippets.
- Copies a shareable diagnosis link with the current date and time zone.
- Copies a PR review comment plus OpenAPI/TypeScript guardrails for date-only fields.
- Runs fully locally: no backend, no analytics, no dependencies.

## Support

If it saved you a production bug: https://ko-fi.com/quarkassistant

Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision.
