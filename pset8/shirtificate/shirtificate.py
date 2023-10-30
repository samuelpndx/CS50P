from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png",y =80, w=190, keep_aspect_ratio=True)
        self.set_font("helvetica", size=50)
        self.cell(0, 80, "CS50 Shirtificate", align="C")

    def footer(self):
        self.set_font("helvetica", size=35)
        self.set_text_color(255, 255, 255)
        self.cell(-185,275, f"{get_name()} took CS50", align="C")



def main():
    pdf = PDF(orientation="P",format="A4")
    pdf.add_page()
    pdf.output("shirtificate.pdf")

def get_name():
    return input("What's yout name? ")

if __name__ == "__main__":
    main()