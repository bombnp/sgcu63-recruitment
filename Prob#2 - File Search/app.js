function search(fileToSearch, dirObj, depth, dirName) {
	let directories = []

	for (const [key, value] of Object.entries(dirObj)) {
		if (key == "_files") {
			// assumption: 	The file names inside the array are unique. If not, suppose multiple identical file names
			// 				output only once in the result.
			if (value.includes(fileToSearch)) {
				directories.push({
					depth: depth,
					directory: dirName
				})
			}
		} else {
			let results = search(fileToSearch, value, depth+1, dirName + key + "/")
			directories.push(...results)
		}
	}

	return directories
}

function fileSearch(fileToSearch, filesObj) {
	let jsonFile = require(filesObj)
	let directories = search(fileToSearch, jsonFile, 0, "/")
	
	// sorts by depth, then by directory, then mapped to directory
	directories = directories.sort((a, b) => {
		if (a.depth != b.depth) {
			return a.depth - b.depth
		}
		return a.directory.localeCompare(b.directory)
	}).map((value) => value.directory)
	
	return directories
}

fileSearch("file1", "./dataset.json")