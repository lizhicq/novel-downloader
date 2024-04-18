import unittest
from unittest.mock import patch
from src.downloader import download_novel

class TestDownloader(unittest.TestCase):

    @patch('src.downloader.requests.get')
    def test_download_novel_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'Novel Content Here'
        response = download_novel('http://example.com/novel')
        self.assertEqual(response, 'Novel Content Here')

    @patch('src.downloader.requests.get')
    def test_download_novel_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception):
            download_novel('http://example.com/novel')

if __name__ == '__main__':
    unittest.main()
