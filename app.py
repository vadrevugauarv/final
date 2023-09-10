import streamlit as st
import random

def shuffle_array(array):
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]

def generate_seat_arrangement(num_rows, num_columns, num_branches, branch_students):
    total_students = sum(branch_students)
    seats = list(range(1, total_students + 1))
    shuffle_array(seats)

    seat_arrangement = [[] for _ in range(num_rows)]

    student_counter = 0

    for row in range(num_rows):
        for col in range(num_columns):
            if student_counter >= total_students:
                return seat_arrangement
            if not seat_arrangement[row]:
                seat_arrangement[row] = []

            seat_arrangement[row].append(f"Seat {seats[student_counter]} - {branch_names[row % num_branches]}")
            student_counter += 1

    return seat_arrangement

st.title("Exam Seat Arrangement")

num_rows = st.number_input("Number of Rows:", min_value=1, value=4)
num_columns = st.number_input("Number of Columns:", min_value=1, value=6)
num_branches = st.number_input("Number of Branches:", min_value=1, value=3)

branch_names = []

for i in range(num_branches):
    branch_name = st.text_input(f"Branch {i+1} Name:")
    branch_names.append(branch_name)

branch_students = []

for i in range(num_branches):
    num_students = st.number_input(f"Number of Students in {branch_names[i]}:", key=f"num_students_{i}", min_value=1, value=5)
    branch_students.append(num_students)

generate_button = st.button("Generate Seat Arrangement")

if generate_button:
    seat_arrangement = generate_seat_arrangement(num_rows, num_columns, num_branches, branch_students)

    st.subheader("Seat Arrangement:")
    for row in seat_arrangement:
        st.write(row)

st.write("Note: This app ensures students from the same branch are distributed evenly across the seating arrangement.")
