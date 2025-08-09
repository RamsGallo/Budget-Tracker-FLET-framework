import flet as ft
import datetime as dt
import time

def main(page:ft.Page):
    page.window_max_height=700
    page.window_max_width=350
    page.window_resizable=False
    page.theme_mode=ft.ThemeMode.LIGHT
    page.bgcolor=ft.colors.GREY_100
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.START
    page.title="Budget Tracker"
    page.fonts={
        "Aleo Bold Italic": "https://raw.githubusercontent.com/google/fonts/master/ofl/aleo/Aleo-BoldItalic.ttf"}
    page.theme=ft.Theme(font_family="Aleo Bold Italic")
    
    def adjust_bal(e):
        adjust_bal_textfield.visible=True
        adjust_bal_textfield.on_focus=True
        adjust_bal_btn.visible=True
        dd_currency.visible=True
        bal_btn_close.visible=True
        adjust_btn.icon=ft.icons.ARROW_DROP_DOWN
        page.update()
        
    def set_bal(e):
        try:
            if adjust_bal_textfield.value and dd_currency.value:
                balance.label=dd_currency.value
                #balance.value = "{:,}".format(int(adjust_bal_textfield.value))
                balance.value=round(float(adjust_bal_textfield.value),2)
                #round(balance.value, 2)
                adjust_bal_textfield.value=''
                dd_currency.visible=False
                adjust_bal_textfield.visible=False
                adjust_bal_btn.visible=False
                bal_btn_close.visible=False
                adjust_btn.icon=ft.icons.ARROW_DROP_UP
                total_expense.suffix_text=dd_currency.value
                total_income.suffix_text=dd_currency.value
            else:
                page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Missing values | Fields cannot be empty"), duration=1500, open=True)
        except:
            page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Type mismatch"), duration=1500, open=True)
        page.update()
        
    def close_adjust(e):
        adjust_bal_textfield.visible=False
        dd_currency.visible=False
        adjust_bal_btn.visible=False
        bal_btn_close.visible=False
        adjust_btn.icon=ft.icons.ARROW_DROP_UP
        page.update()
        
    def btn_open_expense(e):
        expense_title.visible=True
        total_expense.visible=True
        dd_category_expense.visible=True
        btn_set_expense.visible=True
        btn_expense_open.icon=ft.icons.ARROW_DROP_DOWN
        btn_income_open.icon=ft.icons.ARROW_DROP_UP
        
        income_title.visible=False
        total_income.visible=False
        dd_category_income.visible=False
        btn_set_income.visible=False
        page.update()
        
    def btn_open_income(e):
        income_title.visible=True
        total_income.visible=True
        dd_category_income.visible=True
        btn_set_income.visible=True
        btn_expense_open.icon=ft.icons.ARROW_DROP_UP
        btn_income_open.icon=ft.icons.ARROW_DROP_DOWN
        
        expense_title.visible=False
        total_expense.visible=False
        dd_category_expense.visible=False
        btn_set_expense.visible=False
        page.update()
    
    def hide_expense_income(e):
        expense_title.visible=False
        total_expense.visible=False
        dd_category_expense.visible=False
        btn_set_expense.visible=False
        btn_expense_open.icon=ft.icons.ARROW_DROP_UP
        btn_income_open.icon=ft.icons.ARROW_DROP_UP
        
        income_title.visible=False
        total_income.visible=False
        dd_category_income.visible=False
        btn_set_income.visible=False
        page.snack_bar=ft.SnackBar(content=ft.Text("Input field closed"), duration=1500, open=True)
        page.update()
    
        
    def set_expense_func(e):
        try:
            if balance.value and total_expense.value and dd_category_expense.value:
                balance.value=float(balance.value)-float(total_expense.value)
                round(balance.value, 2)
                view_history_col.controls.insert(0, ft.Container(content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_CIRCLE_DOWN_SHARP),
                        ft.Column(
                            controls=[
                                ft.Text(value=f"{dd_category_expense.value}", size=14,),
                                ft.Text(f"{current_date}", size=10,),
                            ], expand=1, 
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(f" -{float(total_expense.value)}", size=14),
                                ft.Text(),
                            ],
                        ),
                    ]
                ),)
                )
                total_expense.value=''
            else:
                page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Missing values | Fields cannot be empty"), duration=1500, open=True)
        except:
            page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Type mismatch"), duration=1500, open=True)
        page.update()
        
    def set_income_func(e):
        try:
            if balance.value and total_income.value and dd_category_income.value:
                balance.value=float(balance.value)+float(total_income.value)
                round(balance.value, 2)
                view_history_col.controls.insert(0, ft.Container(content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_CIRCLE_UP_SHARP),
                        ft.Column(
                            controls=[
                                ft.Text(value=f"{dd_category_income.value}", size=14,),
                                ft.Text(f"{current_date}", size=10,),
                            ], expand=1, 
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(f" +{float(total_income.value)}", size=14),
                                ft.Text(),
                            ],
                        ),
                    ]
                ),)
                ),
                total_income.value='' 
            else:
                page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Missing values | Fields cannot be empty"), duration=1500, open=True)        
        except:
            page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Type mismatch"), duration=1500, open=True)
        page.update()
    
    def append_goal(e):
        try:
            if goal_name.value and goal_target_amount.value and goal_current_amount.value:
                we=float(goal_current_amount.value)/float(goal_target_amount.value)
                we_s=we*100
                we_ss=round(we_s, 2)
                set_goal_col.controls.append(ft.Container(
                    content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.ARROW_CIRCLE_UP_SHARP),
                        ft.Column(
                            controls=[
                                #print(goal_name.value),
                                ft.Text(f"Goal: {goal_name.value} at {we_ss}%", size=14,),
                                ft.Text(f"{today}", size=10,),
                                ft.ProgressBar(color=ft.colors.AMBER, value=we),
                            ], expand=1, 
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(f" Target: {float(goal_target_amount.value)}", size=14),
                                ft.Text(f" Current: {float(goal_current_amount.value)}", size=14),
                                #ft.Text(),
                            ],
                        ),
                    ]
                ),)
                ),
                goal_name.value=''
                goal_current_amount.value=''
                goal_target_amount.value=''
            else:
                page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Missing values | Fields cannot be empty"), duration=1500, open=True) 
        except:
            page.snack_bar=ft.SnackBar(content=ft.Text("Input Error: Type mismatch"), duration=1500, open=True)
        page.update()
    
    def calc_guide(e):
        try:
            spend_guide_col.controls.clear()
            if balance.value>0:
                amount_week=float(balance.value)/7.0
                amount_month=float(balance.value)/30.0
                round(amount_week, 2)
                round(amount_month, 2)

                spend_guide_col.controls.append(
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.LIGHTBULB_SHARP),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"My balance"),
                                        ft.Text(f"7-day spending amount"),
                                        ft.Text(f"30-day spending amount")
                                    ], expand=1, 
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(f"{dd_currency.value} {balance.value}"),
                                        ft.Text(f"{dd_currency.value} {round(amount_week, 2)}"),
                                        ft.Text(f"{dd_currency.value} {round(amount_month, 2)}"),
                                    ],
                                ),
                            ]
                        ),
                    )
                )
            else:
                page.snack_bar=ft.SnackBar(content=ft.Text("Error: Balance cannot be equal or less than zero."), duration=1500, open=True)
        except:
            page.snack_bar=ft.SnackBar(content=ft.Text("Error: Balance cannot be equal or less than zero."), duration=1500, open=True)
        page.update()
    
    def clear_guide_controls(e):
        spend_guide_col.controls.clear()
        page.update()
    
    #def set_prog_bar(min, max):
    #    return ft.ProgressBar(color="amber", value=min/max)
    
    today=dt.date.today()
    timestamp = time.time()
    current_date = time.ctime(timestamp)
        
    balance=ft.TextField(value="0.0", disabled=True, border="underline", label="PHP")
    
    adjust_bal_textfield=ft.TextField(label="Set balance", visible=False, hint_text="How much money do you have?", border="underline")
    
    adjust_bal_btn=ft.OutlinedButton("Set", visible=False, on_click=set_bal)
    
    bal_btn_close=ft.OutlinedButton("Close", visible=False, on_click=close_adjust)
    
    dd_currency = ft.Dropdown(border="underline",
        options=[
            ft.dropdown.Option("PHP"),
            ft.dropdown.Option("USD"),
            ft.dropdown.Option("GBP"),
        ], 
        label="Currency", visible=False,)
    
    # Expense section
    total_expense=ft.TextField(label="Expense", hint_text="How much did you spend?", border="underline", visible=False)
    
    btn_set_expense=ft.OutlinedButton("Set", visible=False, on_click=set_expense_func)

    expense_title=ft.Text("Set your expenses", visible=False)
    
    dd_category_expense = ft.Dropdown(border="underline",
        options=[
            ft.dropdown.Option("Food & Drinks"),
            ft.dropdown.Option("Shopping"),
            ft.dropdown.Option("Housing"),
            ft.dropdown.Option("Transportation"),
            ft.dropdown.Option("Vehicle"),
            ft.dropdown.Option("Life & Entertainment"),
            ft.dropdown.Option("Communication & Electronics"),
            ft.dropdown.Option("Financial Expenses"),
            ft.dropdown.Option("Investments"),
            ft.dropdown.Option("Other"),
        ], 
        label="Category", visible=False)
    
    # Income section
    total_income=ft.TextField(label="Income", hint_text="How much did you earn?", border="underline", visible=False)
    
    btn_set_income=ft.OutlinedButton("Set", visible=False, on_click=set_income_func)
    
    income_title=ft.Text("Add income to your budget", visible=False)
    
    dd_category_income=ft.Dropdown(border="underline",
        options=[
            ft.dropdown.Option("Income: Checks, coupons"),
            ft.dropdown.Option("Income: Dues & grants"),
            ft.dropdown.Option("Income: Gifts"),
            ft.dropdown.Option("Income: Interests, dividends"),
            ft.dropdown.Option("Income: Lending"),
            ft.dropdown.Option("Income: Lottery, Gambling"),
            ft.dropdown.Option("Income: Refunds"),
            ft.dropdown.Option("Income: Rental income"),
            ft.dropdown.Option("Income: Sale"),
            ft.dropdown.Option("Income: Wage, invoices"),
        ], 
        label="Category", visible=False)
    
    adjust_btn=ft.OutlinedButton("Adjust Balance", on_click=adjust_bal, icon=ft.icons.ARROW_DROP_UP)
    
    head_container = ft.Container(
        content=ft.Column([ft.ResponsiveRow(controls=[
                                    ft.Text(value="Current balance", size=17,),
                                    balance,
                                    adjust_btn,
                                    bal_btn_close,
                                ]),
                           ft.ResponsiveRow(controls=[
                                    adjust_bal_textfield, 
                                    dd_currency, 
                                    adjust_bal_btn
                                ])
                ], #width=float("inf"), scroll=ft.ScrollMode.ALWAYS, spacing=1, height=10,
            ), padding=16, border_radius=5, bgcolor=ft.colors.WHITE, margin=ft.margin.only(left=5, right=5, top=10, bottom=10)
    )
    
    btn_expense_open=ft.OutlinedButton("Set Expense", icon=ft.icons.ARROW_DROP_UP, on_click=btn_open_expense)
    btn_income_open=ft.OutlinedButton("Add Income", icon=ft.icons.ARROW_DROP_UP, on_click=btn_open_income)
    
    EandI_container = ft.Container(
        margin=ft.margin.only(left=12, right=12),
        content=ft.Column([
            ft.ResponsiveRow(controls=[
                ft.Text("Expense & Income", size=15,),
                ft.Text("Calculate my spendings", size=12,)
            ]),
            ft.ResponsiveRow(controls=[
                btn_expense_open,
                btn_income_open,
                ft.OutlinedButton(text="Close", on_click=hide_expense_income)
            ], alignment="center"),
            ft.ResponsiveRow(controls=[
                expense_title,
                income_title,
                total_expense,
                dd_category_expense,
                btn_set_expense,
                total_income,
                dd_category_income,
                btn_set_income,
            ]),
        ]), padding=20, border_radius=5, bgcolor=ft.colors.WHITE,
    )
    
    view_history_col=ft.Column(
            spacing=1,
            height=150,
            width=float("inf"), 
            scroll=ft.ScrollMode.AUTO,)
    
    set_goal_col=ft.Column(
            spacing=1,
            height=150,
            width=float("inf"), 
            scroll=ft.ScrollMode.AUTO,)
    
    history_container=ft.Container(
        padding=20, 
        border_radius=5, 
        bgcolor=ft.colors.WHITE, 
        margin=ft.margin.only(left=12, right=12, top=10, bottom=10),
        content=ft.Column(
            controls=[ft.Text("History Overview", size=15),
                      ft.Text("See my recent records", size=12),
                      view_history_col,],)
    )
    
    spend_guide_col=ft.Column(
            spacing=1,
            height=120,
            width=float("inf"), 
            scroll=ft.ScrollMode.AUTO,)
    
    spend_container=ft.Container(
        padding=20, 
        border_radius=5, 
        bgcolor=ft.colors.WHITE, 
        margin=ft.margin.only(left=12, right=12, bottom=10),
        content=ft.Column(
            controls=[ft.Text("Spending Guide", size=15),
                      ft.Text("How much should I spend per day?", size=12),
                      spend_guide_col,
                      ft.Divider(),
                      ft.Row(controls=[
                            ft.TextButton("Calculate", on_click=calc_guide),
                            ft.TextButton("Clear", on_click=clear_guide_controls)]),
                    
            ],)
    )
    
    def show_goal_field(e):
        goal_name.visible=True
        goal_title.visible=True
        goal_target_amount.visible=True
        goal_current_amount.visible=True
        set_goal.visible=True
        page.update()
        
    def close_goal_field(e):
        goal_name.visible=False
        goal_title.visible=False
        goal_target_amount.visible=False
        goal_current_amount.visible=False
        set_goal.visible=False
        page.update()
    
    goal_name=ft.TextField(label="Goal Name", hint_text="What are you saving for?", border="underline", visible=False)
    
    goal_title=ft.Text("Create a goal by filling out the fields", visible=False, size=12)
    
    goal_target_amount=ft.TextField(label="Target amount", hint_text="How much does this goal cost?", visible=False, border="underline")
    
    goal_current_amount=ft.TextField(label="Saved already", hint_text="How much have you saved so far?", visible=False, border="underline")
    
    set_goal=ft.OutlinedButton("Set Goal", visible=False, on_click=append_goal)
    
    goal_prog_bar=ft.ProgressBar(width=400)
    
    goal_container=ft.Container(
        padding=20, 
        border_radius=5, 
        bgcolor=ft.colors.WHITE, 
        margin=ft.margin.only(left=12, right=12, bottom=10),
        content=ft.Column(
            controls=[
                ft.Text("Set your Goals 🎯", size=15,),
                ft.Text("How much have I saved?", size=12,), 
                set_goal_col,
                ft.Divider(),
                ft.Row(controls=[
                    ft.TextButton("CREATE GOAL", on_click=show_goal_field),
                    ft.TextButton("Close", on_click=close_goal_field)
                    ]
                ),
                ft.ResponsiveRow(
                    controls=[
                        goal_title,
                        goal_name,
                        goal_target_amount,
                        goal_current_amount,
                        set_goal,
                        ]
                ),
                ],
            )
        
    )
    
    tab_1_col = ft.Column(
        spacing=1,
        height=200,
        #width=float("inf"), 
        #scroll=ft.ScrollMode.AUTO,
        controls=[head_container, 
                  #ft.Divider(),
                  ft.Column(
                    controls=[
                        EandI_container,
                        history_container,
                        spend_container,
                        goal_container,
                    ], 
                    spacing=1,
                    height=200, 
                    width=float("inf"), 
                    scroll=ft.ScrollMode.AUTO, 
                    expand=1)
        ],
        
    )
    
    t = ft.Tabs(
        selected_index=0,
        animation_duration=250,
        tabs=[
            ft.Tab(
                text="Dashboard",
                icon=ft.icons.DASHBOARD_OUTLINED,
                content=tab_1_col,
            ),
        ],
        expand=1,
    )
    page.add(t) # added 1 variable. The tab controls all
    
ft.app(target=main, view=ft.WEB_BROWSER)
"""
A non-sophisticated budget tracker. Track and modify your balance in a simple way. © github.com/RamsGallo 
Added features: Goal creation, Balance weekly/monthly guide, track recent records
""" 
