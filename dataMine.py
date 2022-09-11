import PyPDF2
import pandas as pd


def pdf_to_txt(page_number):
	pdf_file = open("./gradePDF/grd20221EN.pdf", "rb")
	reader = PyPDF2.PdfFileReader(pdf_file)

	page = reader.getPage(page_number)
	text = page.extract_text()

	txt_file = open("./gradePDF/grd20221EN.txt", "w")
	txt_file.writelines(text)

	txt_file.close()
	pdf_file.close()
	return reader.numPages





def open_files():
	total_page_num = pdf_to_txt(0)  # convert pdf to txt file
	line_start = 21

	csv_file = open("./gradePDF/spring2022.csv", "w")

	six_counter = 0  # lines are just 6 and then a new section appears
	for i in range(total_page_num - 1):
		read_txt_file = open("./gradePDF/grd20221EN.txt", "r")
		lines = read_txt_file.readlines()[line_start:]
		for file_object in lines:
			if six_counter == 6:
				print("----------------------------------------------------")
				csv_file.write("\n")
				six_counter = 0
			a_line = file_object.strip().split()
			# print(a_line)
			for a in a_line:
				print(a)
				csv_file.write(a + ",")
			six_counter += 1

		pdf_to_txt(i + 1)
		read_txt_file.close()
	csv_file.close()


def main():
	open_files()


if __name__ == "__main__":
	main()
