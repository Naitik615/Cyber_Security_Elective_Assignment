# Create folder
mkdir Assignment1

# Move inside folder
cd Assignment1

# Create file
touch notes.txt

# Write into file
echo "Initial Text" > notes.txt

# Append text
echo "Additional Text" >> notes.txt

# Copy file
cp notes.txt notes_copy.txt

# Move/Rename file
mv notes_copy.txt moved_notes.txt

# Check file existence
test -f notes.txt && echo "File exists"

# List files
ls

# Change permission
chmod 600 notes.txt
