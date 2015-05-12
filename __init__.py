from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#todos class
class todos(object):
    todo = ["Feed dogs", "Finish laundry", "Do Homework", "Call vet", "Get drycleaning"]
    length = len(todo)
    
    def update(self):
        self.length = len(self.todo)
    
    def add(self, msg):
        self.todo.append(msg)
        self.update()
    
    def remove(self, x):
        self.todo.remove(x)
        self.update()
        
mylist = todos()
#Finish todo class

@app.route('/', methods =['GET', 'POST'])
def todoList():
    try:
        
        if request.method == 'POST':
            if request.form['toAdd'] != "Put a new todo here!":
                add = request.form['toAdd']
                mylist.add(add)
                print "Adding!"
            elif request.form['toRemove'] != "Put a done todo here!":
                rem = request.form['toRemove']
                mylist.remove(rem)
                print "Removing!"
            return redirect(url_for("todoList"))
        else:
            return render_template("index.html", mylist=mylist)
    except Exception, e:
        return str(e)

@app.route('/about/')
def about():
    return "About Page!"




if __name__ == '__main__':
    app.run()
    
