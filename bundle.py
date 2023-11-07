from tinyBundle import bundle

files = ["src/__main__.py", "src/checker.py", "src/verifier.py"] # Add other files here (like you would with a list)

bundle(files,"out/", 9) # out/ is the default output location