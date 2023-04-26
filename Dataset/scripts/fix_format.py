# Append the optimum value to the beginning of each file in the large_scale
# folder

with open('filenames.txt') as f:
    filenames = f.readlines()

for file in filenames:
    with open('../large_scale_optimum/' + file.strip()) as f:
        optimum = f.readlines()[0]
    with open('../large_scale/' + file.strip(), 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(optimum.strip() + '\n' + content)
