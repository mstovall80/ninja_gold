from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,"index.html")

def process_money(request):
    if request.POST['find_gold'] == 'Farm': 
        num = random.randint(10, 20)
        request.session['gold'] += num
        request.session['activities'].append(f" earned {num} gold from the farm!")
    if request.POST['find_gold'] == 'Cave': 
        num = random.randint(5, 10)
        request.session['gold'] += num
        request.session['activities'].append(f" Earned {num} gold from the Cave!")
    if request.POST['find_gold'] == 'House': 
        num = random.randint(2, 5)
        request.session['gold'] += num
        request.session['activities'].append(f" Earned {num} gold from the House!")
    if request.POST['find_gold'] == 'Casino': 
        num = random.randint(0, 50)
        request.session['gold'] += num
        request.session['gold'] -= num
        request.session['activities'].append(f" Earned {num} gold from the Casino!")
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect("/")




