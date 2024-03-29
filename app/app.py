from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'gradesData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Grades Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblGradesImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, grades=result)


@app.route('/view/<int:grades_id>', methods=['GET'])
def record_view(grades_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblGradesImport WHERE id=%s', grades_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', grades=result[0])


@app.route('/edit/<int:grades_id>', methods=['GET'])
def form_edit_get(grades_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblGradesImport WHERE id=%s', grades_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', grades=result[0])


@app.route('/edit/<int:grades_id>', methods=['POST'])
def form_update_post(grades_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldLastName'), request.form.get('fldFirstName'), request.form.get('fldSsn'),
                 request.form.get('fldTest1'), request.form.get('fldTest2'),
                 request.form.get('fldTest3'), request.form.get('fldFinal'), request.form.get('fldGrade'), grades_id)
    sql_update_query = """UPDATE tblGradesImport t SET t.fldLastName = %s, t.fldFirstName = %s, t.fldSsn = %s, 
    t.fldTest1 = %s, t.fldTest2 = %s, t.fldTest3 = %s, t.fldFinal = %s, t.fldGrade = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/grades/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Grades Form')


@app.route('/grades/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldLastName'), request.form.get('fldFirstName'), request.form.get('fldSsn'),
                 request.form.get('fldTest1'), request.form.get('fldTest2'),
                 request.form.get('fldTest3'), request.form.get('fldFinal'), request.form.get('fldGrade'))
    sql_insert_query = """INSERT INTO tblGradesImport (fldLastName,fldFirstName,fldSsn,fldTest1,fldTest2,fldTest3,
    fldFinal,fldGrade) VALUES (%s, %s,%s, %s,%s, %s,%s,%s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:grades_id>', methods=['POST'])
def form_delete_post(grades_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblGradesImport WHERE id = %s """
    cursor.execute(sql_delete_query, grades_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/grades', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblGradesImport')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/grades/<int:grades_id>', methods=['GET'])
def api_retrieve(grades_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblGradesImport WHERE id=%s', grades_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/grades/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/grades/<int:grades_id>', methods=['PUT'])
def api_edit(grades_id) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/grades/<int:grades_id>', methods=['DELETE'])
def api_delete(grades_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
