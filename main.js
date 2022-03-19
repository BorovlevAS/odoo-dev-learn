# some comment line
# prev code was wrong

const tPost = {
	author: 'Artem',
};

const fnAddPost = (tPost, sMessage, dateAdd = Date()) => {
	const newPost = {
		...tPost,
		message: sMessage,
		dateAdd
	}
	
	console.log(newPost);
	
	return newPost;
}

console.log(fnAddPost(tPost, 'Hi there!'));