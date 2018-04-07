from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
app = Flask(__name__)

engine = create_engine('sqlite:///catalogitem.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#All categories
@app.route('/')
@app.route('/catalog')
def showCategories():
    #return "This page will show all my categories."
    categories = session.query(Category).all()
    return render_template('categories.html', categories = categories)

@app.route('/catalog/new', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        flash("New category %s created!" % newCategory.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')
    #return "This page will be for making a new category."


@app.route('/catalog/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
        session.add(category)
        session.commit()
        flash("Category %s successfully edited." % category.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category = category)
    #return "This page will be for editing category %s" % category_id


@app.route('/catalog/<int:category_id>/delete', methods=['GET',
           'POST'])
def deleteCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(category)
        session.commit()
        flash("Category %s successfully deleted." % category.name)
        return redirect(url_for('showCategories'))
    else:
        return render_template('deleteCategory.html', category = category)
    #return "This page will be for deleting category %s" % category_id

@app.route('/catalog/<int:category_id>')
@app.route('/catalog/<int:category_id>/items')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('item.html', category = category, items = items)
    #return "This page is the item for category %s" % category_id


@app.route('/catalog/<int:category_id>/items/new', methods=['GET', 'POST'])
def newItem(category_id):

    if request.method == 'POST':
        item = Item(name=request.form['name'], description=request.form['description'], category_id=category_id)
        session.add(item)
        session.commit()
        flash("New item %s created." % item.name)
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('newItem.html', category_id = category_id)
        #return "This page is for making a new item item for category %s" % category_id

@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit', methods=['GET','POST'])
def editItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        session.add(item)
        session.commit()
        flash("Catalog item %s updated." % item.name)
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('editItem.html', category_id = category_id, item = item)
        #return "This page is for editing item %s" % item_id


@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete', methods=['GET','POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash("Item %s deleted." % item.name)
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('deleteItem.html', category_id = category_id, item = item)
        #return "This page is for deleting item %s" % item_id

# Returning JSON
@app.route('/catalog/JSON')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(Categories=[r.serialize for r in categories])

@app.route('/catalog/<int:category_id>/items/JSON')
def categoryItemJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])

@app.route('/catalog/<int:category_id>/items/<int:item_id>/JSON')
def itemItemJSON(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id = item_id).all()
    return jsonify(Item=[item.serialize])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
