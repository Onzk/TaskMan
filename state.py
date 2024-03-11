from flask import Flask, render_template, request, redirect, flash
from queue import SimpleQueue, LifoQueue, PriorityQueue
from core.task_queue import TaskQueue
from core.task_stack import TaskStack

from models.task import Task
from models.category import Category

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

task_list, task_file, task_stack = [], TaskQueue(), TaskStack()

sub_status = "all"

sort_by = "default"

search = ""

root = Category("root")
