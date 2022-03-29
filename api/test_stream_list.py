
from api.test_case_api import TestCaseApi


class TestStreamList(TestCaseApi):

    def test_stream_one(self):
        response = self.makeGetRequest('stream/1')
        assert response.status_code == 200

        json = response.json()

        assert json['url'] == 'http://httpbin.org/stream/1'
        assert json['headers']['Host'] == 'httpbin.org'

    def test_stream_1000(self):
        rows_count = 5
        response = self.makeGetRequest('stream/' + str(rows_count))
        assert response.status_code == 200

        rows = response.text.split('\n')
        assert len(rows) - 1 == rows_count

    def test_stream_negative_path_var(self):
        response = self.makeGetRequest('stream/-10')
        assert response.status_code == 404

    def test_stream_very_large_var(self):
        response = self.makeGetRequest('stream/999999999999999999999999999999')
        assert response.status_code == 200

        rows = response.text.split('\n')
        assert len(rows) - 1 == 100
