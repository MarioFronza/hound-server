<h1 align="center">Hound Server</h1>

<p align="center">Hound is a simple chat developed using Flask and React Native</p>

<p align="center">
  <a href="http://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License MIT">
  </a>
</p>

<hr />

## Dependencies

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Pip](https://pypi.org/project/pip/)
- [Docker](https://www.docker.com/)

## Prerequisites

To run this server you will need one container running on your machine.

To do so, you will need to run this command:

- `docker run --name postgres -p 5432:5432 -d -t postgres`

## Getting started

1. Clone this repo using `https://github.com/MarioFronza/hound-server.git`
2. Move to the appropriate directory: `cd hound-server`.
3. Create a virtualenv.
4. Create `config.py` file.
5. Run `pip install -r requirements.txt` to install dependencies.
6. Run `python run.py runserver` to see the example app at `http://localhost:5000`.

<!-- ## Tests

To run all tests suites execute this command on the server directory:

- `yarn test`

## Documentation

You can see all the api documentation in this [HTML file](docs/output.html). Just open it in your browser. -->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
