from flask import Flask, render_template, request, redirect, flash
from queue import SimpleQueue, LifoQueue

from models.task import Task
from models.category import Category

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

task_list, task_file, task_stack = [], SimpleQueue(), LifoQueue

sub_status = "all"

sort_by = "default"

root = Category("root")
