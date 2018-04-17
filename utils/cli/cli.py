from utils.cli.cli_handlers import run_test


def register_cli(app):
    @app.cli.command()
    def tests_run():
        """ Run application tests"""
        return run_test.run()
