# some comment line
# prev code was wrong

const tPost = {
	author: 'Artem',
	defs: {
		main1: 'main1',
		main2: 'main2'
	}
};

const fnAddPost = (tPost, sMessage, dateAdd = Date()) => {
	const newPost = {
		...tPost,
		message: sMessage,
		dateAdd
	}
	
	newPost.defs.main1 = 'Here';
	
	return newPost;
}
const aPost = fnAddPost(tPost, 'Hi there!');

console.log(aPost);
console.log(tPost);