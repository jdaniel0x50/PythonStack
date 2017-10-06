from flask import Flask, redirect, render_template, request, session
import random, datetime, math

app = Flask(__name__)
app.secret_key = "MySecretKey@!"
# force cache refresh for all file requests, including style sheets
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def generate_string(new_gold, building):
    if new_gold < 0:
        text_color = 'redtext'
        gain_loss = 'lost'
        post_string = '.. Ouch ...'
    else:
        text_color = 'greentext'
        gain_loss = 'earned'
        post_string = '.. Nice!'
    if building == 'casino':
        pre_string = 'Entered a casino and ' + gain_loss + ' ' + str(int(math.fabs(new_gold))) + ' gold.' + post_string
    else:
        pre_string = 'Earned ' + str(new_gold) + ' gold from the ' + building + '!'
    # html_string = "<p class='" + text_color + "'>" + pre_string
    return (text_color, pre_string)

@app.route('/', methods=['GET', 'POST'])
def index():
    if not session.has_key('total_gold'):
        # init total gold value and activity list
        session['total_gold'] = 0
        session['activity'] = []
        session['visibility'] = 'hide'
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    # gather building type that generated route
    building = request.form['building']

    if building == 'farm':
        new_gold = random.randrange(10, 21)
        (text_color, activity_string) = generate_string(new_gold, building)
    elif building == 'cave':
        new_gold = random.randrange(5, 11)
        (text_color, activity_string) = generate_string(new_gold, building)
    elif building == 'house':
        new_gold = random.randrange(2, 6)
        (text_color, activity_string) = generate_string(new_gold, building)
    elif building == 'casino':
        earn_take = random.randrange(-1, 1)
        new_gold = random.randrange(0, 50)
        if earn_take < 0:
            new_gold *= -1
        (text_color, activity_string) = generate_string(new_gold, building)
    elif building == 'restart':
        session.pop('total_gold')
        session.pop('activity')
        return redirect('/')
    session['total_gold'] += new_gold
    session['visibility'] = 'visible'
    
    print activity_string
    print datetime.datetime.now()
    timeyear = str(datetime.datetime.now().year)
    timemonth = str(datetime.datetime.now().month)
    timeday = str(datetime.datetime.now().day)
    timehour = str(datetime.datetime.now().hour)
    timeminute = str(datetime.datetime.now().minute)
    activity_string_add = activity_string + " (" + timeyear + "-" + timemonth + "-" + timeday + " " + timehour + ":" + timeminute + ")"
    # session['text_color'].append(text_color)
    session['activity'].append((text_color, activity_string_add))

    return redirect('/')

app.run(debug=True) # run our server
