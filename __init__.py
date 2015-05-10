from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def hello_world():
    try:
        #todo = ["Feed dog", "Finish laundry"]
        class todos(object):
            todo = ["Feed dogs", "Finish laundry", "Do Homework", "Call vet", "Get drycleaning"]
            length = len(todo)
            
            def update(self):
                length = len(todo)
            
            def add(self, msg):
                todo.append(msg)
                update()
            
            def remove(self, x):
                todo.remove(x)
                update()
            
            
        mylist = todos()
        
        
        return render_template("index.html", mylist=mylist)
    except Exception, e:
        return str(e)

@app.route('/about/')
def about():
    return "About Page!"




if __name__ == '__main__':
    app.run()
    
