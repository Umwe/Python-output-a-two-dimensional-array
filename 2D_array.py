
print("Chapter 2 Test by Kwizera Africa Hubert Bonaparte")
months = [
    ["January", "February", "March"],
    ["April", "May", "June"],
    ["July", "August", "September"],
    ["October", "November", "December"]
]


row = 0
col = 0

while row < len(months):
    month = months[row][col]
    print(month)
    
    col += 1
    if col >= len(months[row]):
        col = 0
        row += 1
