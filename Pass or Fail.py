def calculate_grade(aggregate_percentage):
	if aggregate_percentage > 75:
		return "Distinction"
	if aggregate_percentage >= 60:
		return "First Division"
	if aggregate_percentage >= 50:
		return "Second Division"
	if aggregate_percentage >= 40:
		return "Third Division"
	else:
		return "Fail"
def main():
	num_courses = int(input())

	marks = list(map(int, input().split()))

	if any(mark < 40 for mark in marks):
		print("Fail")
		return

	aggregate_percentage = sum(marks) / num_courses
	grade = calculate_grade(aggregate_percentage)

	print(f"Aggregate Percentage: {aggregate_percentage:.2f}")
	print(f"Grade: {grade}")

if __name__ == "__main__":
	main()
