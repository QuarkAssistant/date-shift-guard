import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StaticDateShiftGuardTests(unittest.TestCase):
    REQUIRED_FOOTER = "Built by Quark Assistant — autonomous AI agent. Code authored by AI under owner supervision."

    @classmethod
    def setUpClass(cls):
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")

    def test_public_page_has_conversion_surfaces(self):
        for snippet in [
            'https://ko-fi.com/quarkassistant',
            'Tip on Ko-fi',
            'Saved a rollback? Tip $3',
            'id="shareBtn"',
            'Share this guard',
            'id="copyReviewBtn"',
            'Copy PR review comment',
            'id="copyLinkBtn"',
            'Copy diagnosis link',
            'currentDiagnosticUrl',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_share_and_copy_have_clipboard_fallbacks(self):
        for snippet in [
            'navigator.share',
            'navigator.clipboard',
            'document.execCommand(\'copy\')',
            'shareText',
            'Native share failed; copied share text instead.',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_guardrail_pack_is_copyable_and_value_aligned(self):
        for snippet in [
            'id="copyGuardrailBtn"',
            'Copy OpenAPI + TypeScript guardrail',
            'id="guardrailPack"',
            'function guardrailSnippet',
            'format: date',
            'type DateOnlyString',
            'do not call new Date',
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_public_metadata_privacy_and_disclosure_exist(self):
        for snippet in [
            '<link rel="canonical" href="https://quarkassistant.github.io/date-shift-guard/">',
            '<meta property="og:url" content="https://quarkassistant.github.io/date-shift-guard/">',
            '<meta name="twitter:card" content="summary">',
            'browser-only · no tracking · no dependencies',
            self.REQUIRED_FOOTER,
        ]:
            with self.subTest(snippet=snippet):
                self.assertIn(snippet, self.index)

    def test_robots_and_sitemap_point_to_live_url(self):
        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn('Sitemap: https://quarkassistant.github.io/date-shift-guard/sitemap.xml', robots)
        self.assertIn('https://quarkassistant.github.io/date-shift-guard/', sitemap)
        self.assertIn('<changefreq>daily</changefreq>', sitemap)


if __name__ == "__main__":
    unittest.main()
