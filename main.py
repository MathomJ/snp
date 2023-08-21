reference = input("Enter the reference genome: ")

compared = input("Enter a genome to be compared with the reference: ")

for i in range(len(compared)):
    if compared[i] != reference[i]:
        print("-----------------------------------------------------")
        print(f"Difference found at index {i} in compared genome.")

        reference_cpy = reference[:i] + "-" + reference[i] + "-" + reference[(i + 1):]
        compared_cpy = compared[:i] + "-" + compared[i] + "-" + compared[(i + 1):]

        print(f"Reference: {reference_cpy}")
        print(f"Comparison: {compared_cpy}")
        print("-----------------------------------------------------")



