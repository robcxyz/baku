from baku import consts, environment, utils
from contextlib import redirect_stdout
import os
import shutil
import unittest


class TestEnvironment(unittest.TestCase):
    def tearDown(self):
        os.chdir('..')
        if os.path.exists('testrun'):
            shutil.rmtree('testrun')


    def setUp(self):
        utils.ensure_path('testrun')
        os.chdir('testrun')


    def test_initialize(self):
        self.assertFalse(environment.is_blog())
        self.assertFalse(
            os.path.exists(os.path.join('templates', consts.POST_TEMAPLTE)))

        # Silence print() from called function
        with redirect_stdout(None):
            environment.initialize()

        self.assertTrue(environment.is_blog())
        self.assertTrue(
            os.path.exists(os.path.join('templates', consts.POST_TEMAPLTE)))


    def test_load_config(self):
        # Silence print() from called function
        with redirect_stdout(None):
            environment.initialize()

        config = environment.load_config()

        self.assertEqual(config['author'], 'John Doe')
