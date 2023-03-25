from translation import create_app

app = create_app()

if __name__ == "__main__":
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5001))
    app.run(debug=True, host=host, port=port)
