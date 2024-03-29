from tkinter import *


class Converter:
    def __init__(self):

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar ()
        self.var_feedback.set ("")

        self.var_has_error = StringVar ()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="Temperature Converter",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from centigrade to Fahrenheit."

        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       width=40,
                                       justify="left")

        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        "Please enter a number"
        self.temp_error = Label(self.temp_frame, text="",
                                fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Degrees C",
                                        bg="#990099",
                                        fg="#FFFFFF",
                                        font=button_font, width=12
                                        )
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheit_button = Button(self.button_frame,
                                          text="To Farenheit",
                                          bg="#009900",
                                          fg=button_fg,
                                          font=button_font, width=12,
                                          command=lambda: self.temp_convert(-459))
        self.to_farenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#ffffff",
                                     font=button_font, width=12,
                                     command=lambda: self.temp_convert(-273))
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                        text="History / Export",
                                        bg="#004C99",
                                        fg=button_fg,
                                        font=button_font, width=12)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)

    def check_temp(self, min_value):

        error = f"Enter a value more than {min_value}"

        try:
            response = float(self.temp_entry.get())

            if response < min_value:

                # Sets var_has_error so that entry box and
                # labels can be correctly formatted by fomatting function
                # if has_error == "yes" :
                self.var_has_errors.set("yes")
                self.var_feedback.set(error)
                return "invalid"

            # If we have no errors...
            else:
                # set to 'no' in case of previous errors
                self.var_has_errors.set("no")

                # return number to be
                # converted and enable history button
                self.to_history_button.config(state=NORMAL)
                return response

@staticmethod
def round_ans(val):
    var_rounded = (val * 2+ 1) // 2
    return "{:.0f}".format(var_rounded)

# check temperature is valid and convert it
def temp_convert(self, min_val):
    to_convert = self.check_temp(min_val)
    deg_sign = U'\N{DEGREE SIGN}'
    "yes"
    answer = ""
    from_to = ""

    if to_convert == "invalid":
        "no"

        # Convert to Celsius
    elif min_val == -459:
        # do calculation
        answer = (to_convert - 32) * 5 / 9
        from_to = "{} F{} is {} C{}"

        # convert to Farenheit
    else:
        answer = to_convert *1.8 + 32
        from_to = "{} C{} is {} F{}"

    if set_feedback == "yes":
        to_convert = self.round_ans(to_convert)
        answer = self.round_ans(answer)

        # create user output and add to calculation history
        feedback = from_to.format(to_convert, deg_sign,
                                  answer, deg_sign)
        self.var_feedback.set(feedback)

        self.all_calculations.append(feedback)

        # Delete code below when history component is working!
        print(self.all_calculations)

    self.output_answer ()


    except Value Error:
           self.var_feedback.set(error)
           return "invalid"

    # check temperature is more than -459 and convert it

        print(the_number)

    # Shows user output and clears entry widget
    # if ready for next calculation

    def output_answer(self):

        feedback_message = self.var_feedback.get()
        has_errors = self.var_has_errors.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.temp_error.config(fg="#9C0000")
            self.temp_error.config(bg="#F8CECC")

        else:
            self.temp_error.config(fg="#004C00")
            self.temp_error.config(bg="#FFFFFF")

        self.temp_error.config(text=feedback_message)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
