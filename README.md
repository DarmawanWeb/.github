<div align="center">

<img src="assets/logo.svg" width="96" alt="Darmawan Web logo">

# DarmawanWeb/.github

**The organization profile of [Darmawan Web](https://github.com/DarmawanWeb): the [profile README](profile/README.md), the
logo and banner, and the metrics rendered from the organization's repositories.**

[![metrics](https://github.com/DarmawanWeb/.github/actions/workflows/metrics.yml/badge.svg)](https://github.com/DarmawanWeb/.github/actions/workflows/metrics.yml)

</div>

| Path | |
|---|---|
| `profile/README.md` | shown on [github.com/DarmawanWeb](https://github.com/DarmawanWeb) |
| `assets/logo.svg`, `assets/avatar.png`, `assets/banner.png` | logo, the organization's profile picture (512 × 512), profile banner |
| `metrics/*.svg` | overview, languages, featured repositories, lines of code |
| `.github/workflows/metrics.yml` | renders the metrics with [lowlighter/metrics](https://github.com/lowlighter/metrics) every 12 hours, on demand, and when the workflow changes |

The workflow needs a `METRICS_TOKEN` repository secret: a classic personal access token with the `repo`,
`read:org` and `read:user` scopes, so private repositories count towards the languages without being named.
Run it by hand with `gh workflow run metrics -R DarmawanWeb/.github`.
