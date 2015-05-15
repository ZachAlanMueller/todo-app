from flask import Flask, render_template, request, redirect, url_for
import redis
app = Flask(__name__)


r = redis.StrictRedis(host='localhost', port=6379) 
"""
r.lpush('list', "Do Dishes")
r.lpush('list', "Do Laundry")
length_array = r.llen('list')
"""

"""
class todos(object):
        todo = []
        length = 0
        
        def __init__(self):
            r.delete('list') # TO BE DELETED LATER!!
            r.lpush('list', "Example task") # TO BE DELETED LATER!!
            self.update()
         
        def update(self):
            a = []
            for x in range(0,r.llen('list')):
                a.append(r.lindex('list', x))
            l = len(a)
            return a, l    
                 
        def add(self, msg):
             r.lpush("list", msg)
             self.update()
         
        def remove(self, x):
             r.lrem("list", 0, x)
             self.update()
            

mylist = todos();

mylist = ["Feed dogs", "Eat Breakfast", "Do Homework"]
"""
length = 0
mylist = []

def find(string):
    for x in range(0, r.llen('list')):
        if r.lindex('list', x) == string:
            return True, x
    
    return False, -1


def update():
    l = []
    for x in range(0, r.llen('list')):
        l.append(r.lindex('list', x))
    rel = len(l)
    return l, rel

mylist, length = update()

def call():
    global mylist
    global length
    mylist, length = update()

call()
for x in range(0, len(mylist)):
    print mylist[x]
print length






@app.route('/', methods =['GET', 'POST'])
def todoList():
    try:
        
        if request.method == 'POST':
            if request.form['submit'] == "Add Task":
                task = request.form['inputField']
                r.lpush('list', task)
                call()
                print "Adding " + task + " to the list!" 
            elif request.form['submit'] == "Remove Task":
                rem = request.form['inputField']
                proceed, index = find(rem)
                if proceed:
                    r.lrem('list', 0, rem)
                    print "Removing!"
                    call()
                else:
                    print "Element not in list"
                    call()
                
                
            return redirect(url_for("todoList"))
        else:
            return render_template("index.html", mylist=mylist, length=length)
        """
        return render_template("index.html", mylist=mylist)
        """
    except Exception, e:
         return str(e)






if __name__ == '__main__':
    app.run()
    
