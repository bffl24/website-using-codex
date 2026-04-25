from flask import Blueprint, render_template


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def landing():
    return render_template("landing.html")


@main_bp.route("/register")
def register():
    return render_template("register.html")


@main_bp.route("/login")
def login():
    return render_template("login.html")


@main_bp.route("/logout")
def logout():
    return "Logout - coming in Step 3"


@main_bp.route("/profile")
def profile():
    return "Profile page - coming in Step 4"


@main_bp.route("/expenses/add")
def add_expense():
    return "Add expense - coming in Step 7"


@main_bp.route("/expenses/<int:expense_id>/edit")
def edit_expense(expense_id):
    return f"Edit expense {expense_id} - coming in Step 8"


@main_bp.route("/expenses/<int:expense_id>/delete")
def delete_expense(expense_id):
    return f"Delete expense {expense_id} - coming in Step 9"
