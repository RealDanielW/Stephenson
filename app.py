@app.route('/')
def index():
    return render_template('index.html', background_color="#222222")
