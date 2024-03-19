from tkinter import *
from functools import partial  # to prevent unwanted windows


class Converter:

    def __init__(self):

        # initialise variables (such as the feedback variable)
        self.to_history_export_button = None
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # set up GUI frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold")
                                  )
        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and " \
                       "then press one of the buttons to convert " \
                       "it from Centigrade to Fahrenheit."
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wrap=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font=("Arial", "14")
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.temp_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # conversion, help and history / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame,
                                        text="To Celsius",
                                        bg="#990099",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=lambda: self.temp_convert(-459))
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame,
                                           text="To Fahrenheit",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font, width=12,
                                           command=lambda: self.temp_convert(-273))
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_info_button = Button(self.button_frame,
                                          text="Help / Info",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font, width=12,
                                          command=self.to_help)
        from functools import partial  # to prevent unwanted windows

        self.to_help_info_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_export_button = Button(self.button_frame,
                                               text="History / Export",
                                               bg="#004C99",
                                               fg=button_fg,
                                               font=button_font, width=12,
                                               state=DISABLED)

        self.to_history_export_button.grid(row=1, column=1, padx=5, pady=5)

    # checks user input amd if it's valid, converts temperature
    def check_temp(self, min_value):

        has_error = "no"

        # check that user has entered a valid number...

        response = self.temp_entry.get()

        try:
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        # sets var_has_error so that entry box and
        # labels can be correctly formatted by formatting function
        if has_error == "yes":
            error = "Please enter a number greater " \
                    "than {}".format(min_value)

            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # if we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            # return number to be converted and
            # enable history button
            self.to_history_export_button.config(state=NORMAL)
            return response

    @staticmethod
    def round_ans(val):
        var_rounded = (val * 2 + 1) // 2
        return "{:.0f}".format(var_rounded)

    # check temperature is valid and convert it
    def temp_convert(self, min_val):
        to_convert = self.check_temp(min_val)
        degree_sign = u'\N{DEGREE SIGN}'
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        # convert to celsius
        elif min_val == -459:
            # do calculation
            answer = (to_convert - 32) * 5 / 9
            from_to = "{} F{} is {} C{}"

        # convert to fahrenheit
        else:
            answer = to_convert * 1.8 + 3.2
            from_to = "{} C{} is {} F{}"

        if set_feedback == "yes":
            to_convert = self.round_ans(to_convert)
            answer = self.round_ans(answer)

            # create user output and add to calculation history
            feedback = from_to.format(to_convert, degree_sign,
                                      answer, degree_sign)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            # delete code below when history component is working!
            print(self.all_calculations)

        self.output_answer()

    # shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.output_label.config(fg="#9C0000")
            self.temp_entry.config(bg="#F8CECC")

        else:
            self.output_label.config(fg="#004C00")
            self.temp_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_info_button.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)

        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the temperature " \
                    "you wish to convert and then choose to convert " \
                    "to either degrees Celsius (centigrade) or " \
                    "Fahrenheit... \n\n" \
                    " Not that -273 degrees Celsius " \
                    "(-459 Fahrenheit is absolute zero (the coldest possible " \
                    "temperature). If you try to convert a " \
                    "temperature that is less than -273 degrees Celsius, " \
                    "you will get an error message. \n\n " \
                    "to see your calculation history and export it to a " \
                    "text file, please click the 'History / Export' button"
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wrap=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        # put help button back to normal...
        partner.to_help_info_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()