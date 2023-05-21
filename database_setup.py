from blog.settings import db
from datetime import datetime
from bson.objectid import ObjectId

now = datetime.now()


print(db.users.insert_one(
    {
        'name': 'Bhanu Sankhayn',
        'email': 'bhanusankhyan@live.com',
        'password': '12345'
    }
))

db.blogs.insert_one(
    {
        'title': 'Resisting Deterministic Thinking',
        'description': """
        I just returned from a three month sabbatical spent mostly offline diving through history and I feel like I’ve returned to an alien planet full of serious utopian and dystopian thinking swirling simultaneously. I find myself nodding along because both the best case and worst case scenarios could happen. But also cringing because the passion behind these declarations has no room for nuance. Everything feels extreme and fully of binaries. I am truly astonished by the the deeply entrenched deterministic thinking that feels pervasive in these conversations.

        Deterministic thinking is a blinkering force, the very opposite of rationality even though many people who espouse deterministic thinking believe themselves to be hyper rational. Deterministic thinking tends to seed polarization and distrust as people become entrenched in their vision of the future. Returning to the modern world, I’m finding myself frantically waving my hands in a desperate attempt to get those around me to take a deep breath (or maybe 100 of them). Given that few people can see my hand movements from my home office, I’m going to pretend like it’s 2004 and blog my thoughts in the hopes that this post might calm at least one person down. Or, maybe, if I’m lucky, it’ll be fed into an AI model and add a tiny bit of nuance.

        What is deterministic thinking?
        Simply put, determinism is “if x, then y.” It is the notion that if we do something (x), a particular outcome (y) is inevitable. Determinisms are not inherently positive or negative. It is just as deterministic to say “if we build social media, the world will be a more connected place” as it is to say “social media will destroy democracy.”

        It is extraordinarily common for people who are excited about a particular technology to revert to deterministic thinking. And they’re often egged on to do so. Venture capitalists want to hear deterministic thinking in sales pitches. Same with the National Science Foundation. In many social science fields, these futuristic speech acts gets labeled in a pejorative manner as “technological determinism.” Inventors and corporations are often accused of being deterministic, which is a shorthand intended to dismiss their rhetoric as ahistoric and socially oblivious. (Academics who study technological determinism are often more nuanced in this scholarship than their blog posts and op-eds.)

        Meanwhile, however, tech critics often fall into the same trap. Many professional critics (including academics, journalists, advocates) are incentivized to do so because such rhetoric appeals to funders and makes for fantastic opinion pieces. Their rhetoric is rarely labeled deterministic because that’s not the language of futurists. Rather, they are typically dismissed as being clueless about technology and anti-progress. They’re regularly not invited to “the party” (where the technology is being debated by those involved in creating it) because they’re seen as depressing.

        Determinism’s ugly step-sibling is “solutionism.” Solutionism is the belief that x will be a solution not just to achieve y but to achieve all possibly y’s. Solutionists tend to be so enamored with x that they cannot engage with any criticism of x.

        In a world where technologies are given power, authority, and funding, those with positive deterministic views (and solutionistic mindsets) often have more resources and power, leading to a mutually self-destructive polar vortex rich with righteousness that is anything but rational. This is often visible through shouting matches. Right now, the cacophony is overwhelming. And it’s breaking my brain.
        """,
        'image': '',
        'date': now.strftime("%d/%m/%Y %H:%M:%S"),
        'tags': ['Artificial Intelligence', 'Ethics'],
        'user_id': ObjectId("643713ac5d7fdeed07aa4e71")
    }
)
