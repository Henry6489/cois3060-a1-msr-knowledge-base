import unittest
from pathlib import Path


class TestMSRKnowledgeBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        project_root = Path(__file__).resolve().parents[1]
        html_path = project_root / "src" / "index.html"

        cls.html = html_path.read_text(encoding="utf-8")

    def test_data_sources_section_exists(self):
        self.assertIn('id="data-sources"', self.html)

    def test_collection_methods_section_exists(self):
        self.assertIn('id="collection-methods"', self.html)

    def test_analysis_methods_section_exists(self):
        self.assertIn('id="analysis-methods"', self.html)

    def test_publication_venues_section_exists(self):
        self.assertIn('id="publication-venues"', self.html)

    def test_four_navigation_buttons_exist(self):
        count = self.html.count('class="tab-button')
        self.assertEqual(count, 4)


if __name__ == "__main__":
    unittest.main()
