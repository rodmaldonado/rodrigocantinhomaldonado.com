import importlib.util
from pathlib import Path
import unittest


MODULE = Path(__file__).parents[1] / "scripts" / "expand_authority_phase3.py"


def load_module():
    spec = importlib.util.spec_from_file_location("phase3", MODULE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Phase3Tests(unittest.TestCase):
    def test_phase3_has_distinct_substantial_pages(self):
        module = load_module()
        slugs = [page["slug"] for page in module.PAGES]
        self.assertEqual(len(slugs), 9)
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertTrue(all(len(page["intro"]) >= 140 for page in module.PAGES))
        self.assertTrue(all(len(page["sections"]) >= 4 for page in module.PAGES))

    def test_render_includes_required_seo_and_internal_links(self):
        module = load_module()
        output = module.render(module.PAGES[0])
        self.assertEqual(output.count("<h1>"), 1)
        self.assertIn("rel='canonical'", output)
        self.assertIn("application/ld+json", output)
        self.assertIn("BreadcrumbList", output)
        self.assertIn("/artigos/", output)
        self.assertIn("/contato/", output)

    def test_sitemap_entry_is_stable(self):
        module = load_module()
        entry = module.sitemap_entry(module.PAGES[0])
        self.assertIn("<loc>https://rodrigocantinhomaldonado.com/", entry)
        self.assertIn("<lastmod>", entry)
        self.assertNotIn("#", entry)


if __name__ == "__main__":
    unittest.main()
