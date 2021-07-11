from flask import Flask, render_template, request, redirect, send_file
from stackoverflow_scrapper import sof_extract_data
from remote_ok_scrapper import rmok_extract_data
from we_work_remotely_scrapper import wewr_extract_data
from save import save_to_file

"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

app = Flask("JobScrapper")

# fake db
db = {}

@app.route("/")
def home():
  return render_template("final_index.html")


@app.route("/final_scrap")
def scrap():
  search = request.args.get("search")

  if search not in db:
    data_list = []
    data_list = sof_extract_data(search, data_list)
    data_list = rmok_extract_data(search, data_list)
    data_list = wewr_extract_data(search, data_list)
    db[search] = data_list
  else:
    data_list = db[search]
  length = len(data_list)
  return render_template("final_scrap.html", data_list=data_list, search=search, length=length)


@app.route("/export")
def export():
    try:
        search = request.args.get("search")
        print(search)
        if not search:
            print("if not search")
            raise Exception()

        jobs = db.get(search)
        if not jobs:
            print("if not jobs")
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except Exception:
        return redirect("/")

app.run()
