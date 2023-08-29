import json

# Load your JSON data
with open('example.json', 'r') as json_file:
    data = json.load(json_file)

# Function to convert seconds to ASS time format (hh:mm:ss.cs)
def seconds_to_ass_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    centiseconds = int((seconds % 1) * 100)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{centiseconds:02}"

# Create or open the .ass file for writing
with open('output.ass', 'w') as ass_file:
    # Write the ASS file header
    ass_file.write("[Script Info]\n")
    ass_file.write("; Script generated by Aladin Transcripter\n")
    ass_file.write("Title: Your Video Title\n")
    ass_file.write("ScriptType: v4.00+\n")
    ass_file.write("WrapStyle: 0\n")
    ass_file.write("ScaledBorderAndShadow: yes\n")
    ass_file.write("YCbCr Matrix: None\n")
    ass_file.write("[V4+ Styles]\n")
    ass_file.write("Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n")
    ass_file.write("Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1\n")
    ass_file.write("[Events]\n")
    ass_file.write("Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    
    # print(data["results"]["channels"][0]["alternatives"][0]["paragraphs"]["paragraphs"][0]["sentences"])
    
    
    # Convert sentences to ASS format
    ass_lines = []
    for i in range( len(data["results"]["channels"][0]["alternatives"][0]["paragraphs"]["paragraphs"])):
        for sentence in data["results"]["channels"][0]["alternatives"][0]["paragraphs"]["paragraphs"][i]["sentences"]:
            start_time = seconds_to_ass_time(sentence["start"])
            end_time = seconds_to_ass_time(sentence["end"])
            text = sentence["text"]
            ass_lines.append(f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{text}")

# Write ASS lines to a file
with open("output.ass", "a") as ass_file:
    for line in ass_lines:
        ass_file.write(line + "\n")
print("ASS file created successfully.")
