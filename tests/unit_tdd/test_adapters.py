from unittest import TestCase
import inspect
from pydoautomator.adapters import ApiAdapter
import pydoautomator


class TestApiAdapter(TestCase):
    def test_if_submodule_adapters_exists(self):
        try:
            import pydoautomator.adapters as adapters
        except:
            self.fail('submodule adapters does NOT exist')

    def test_if_ApiAdapter_exists(self):
        import pydoautomator.adapters as adapters
        self.assertTrue(hasattr(adapters, 'ApiAdapter'),
                        'ApiAdapter does not exists in adapters')

    def test_ApiAdapter_should_be_a_class(self):
        from pydoautomator.adapters import ApiAdapter
        self.assertTrue(
            inspect.isclass(ApiAdapter),
            'ApiAdapter is NOT a class!'
        )

    def test_if_token_exists(self):
        self.assertTrue(
            hasattr(ApiAdapter, 'token'),
            'token does NOT exist in ApiAdapter'
        )

    def test_constructor_token(self):
        token = 'my-test-123-token'
        api_adapter = ApiAdapter(token)
        self.assertEqual(
            api_adapter.token,
            token
        )

    def test_if_headers_exists(self):
        self.assertTrue(
            hasattr(ApiAdapter, 'headers'),
            'headers does NOT exist in ApiAdapter'
        )

    def test_constructor_headers(self):
        token = 'my-test-123-token'
        headers = {'Authorization': 'Bearer ' + token}
        api_adapter = ApiAdapter(token)
        self.assertEqual(
            api_adapter.headers,
            headers
        )

    def test___session_should_exist_in_ApiAdapter(self):
        self.assertTrue(
            hasattr(ApiAdapter, '_ApiAdapter__session')
        )

    def test_if_adapters_have_Session(self):
        self.assertTrue(
            hasattr(pydoautomator.adapters, 'Session'),
            'adapters does not have Session attr'
        )

    def test_if___session_is_requests_class(self):
        import requests
        self.assertIs(
            pydoautomator.adapters.Session,
            requests.sessions.Session
        )

    def test_if_requests_is_session_instance(self):
        import requests
        self.assertIsInstance(
            ApiAdapter._ApiAdapter__session,
            requests.sessions.Session
        )

    def test_if_requests_exists_in_instance(self):
        token = 'my-test-123-token'
        api_adapter = ApiAdapter(token)
        self.assertTrue(
            hasattr(api_adapter, 'requests'),
            'requests does NOT exists in ApiAdapter instance'
        )

    def test_if_session_headers_are_updated_on_instance(self):
        token = 'my-test-123-token'
        auth_headers = {'Authorization': 'Bearer ' + token}
        api_adapter = ApiAdapter(token)

        self.assertTrue(
            set(auth_headers) <= set(api_adapter._ApiAdapter__session.headers),
            'auth_headers are not being updated on instances session'
        )

    def test_requests_should_be_equal_instance_session(self):
        token = 'my-test-123-token'
        api_adapter = ApiAdapter(token)
        self.assertEqual(
            api_adapter._ApiAdapter__session,
            api_adapter.requests
        )
