STOP_WORDS = [
    'а',
    'абсолютно',
    'автоматически',
    'аккуратно',
    'активно',
    'анализировать',
    'аплодировать',
    'ах',
    'б',
    'бегать',
    'безусловно',
    'беспокоиться',
    'благодарить',
    'благодаря',
    'блестеть',
    'близко',
    'бог',
    'бодрствовать',
    'более',
    'болтать',
    'больно',
    'больше',
    'бормотать',
    'бояться',
    'бриться',
    'будем',
    'будет',
    'будете',
    'будешь',
    'будить',
    'будто',
    'буду',
    'будут',
    'будучи',
    'будь',
    'будьте',
    'бы',
    'был',
    'была',
    'были',
    'было',
    'быстро',
    'быть',
    'в',
    'важно',
    'вам',
    'вами',
    'вас',
    'ваш',
    'вблизи',
    'вверх',
    'вдали',
    'вдвое',
    'вдвоём',
    'вдоль',
    'вдруг',
    'ведь',
    'вежливо',
    'везде',
    'велеть',
    'верить',
    'верно',
    'вероятно',
    'весело',
    'весь',
    'весьма',
    'взглядывать',
    'вздыхать',
    'взрослеть',
    'видеть',
    'видимо',
    'видно',
    'включая',
    'влево',
    'вместе',
    'вместо',
    'вачале',
    'ве',
    'вниз',
    'внизу',
    'вновь',
    'внутри',
    'внутрь',
    'во',
    'во-первых',
    'вовремя',
    'вовсе',
    'возле',
    'возможно',
    'вокруг',
    'волновать',
    'волноваться',
    'вон',
    'вообще',
    'вопрос',
    'восемнадцатый',
    'восемнадцать',
    'восемь',
    'восемьдесят',
    'восемьсот',
    'восклицать',
    'воспринимать',
    'восьмидесятый',
    'восьмой',
    'вот',
    'впервые',
    'вперёд',
    'впереди',
    'вполне',
    'впоследствии',
    'вправо',
    'впрочем',
    'временами',
    'время',
    'вроде',
    'все',
    'всё',
    'всё-таки',
    'всегда',
    'всего',
    'всей',
    'вселять',
    'всем',
    'всём',
    'всеми',
    'всему',
    'всех',
    'всею',
    'всея',
    'вскоре',
    'вслед',
    'вследствие',
    'вслух',
    'встречать',
    'всю',
    'всюду',
    'вся',
    'всякий',
    'второй',
    'втроём',
    'вчера',
    'вы',
    'выглядеть',
    'выдыхать',
    'высказывать',
    'высоко',
    'выучивать',
    'выходить',
    'вычёркивать',
    'выше',
    'выясняться',
    'г',
    'где',
    'где-нибудь',
    'где-то',
    'гладить',
    'глубоко',
    'глупо',
    'глядеть',
    'говорить',
    'говориться',
    'год',
    'года',
    'году',
    'годам',
    'годами',
    'годов',
    'годом',
    'годах',
    'годе',
    'гораздо',
    'гордиться',
    'город',
    'горько',
    'горячо',
    'громко',
    'грубо',
    'гулять',
    'д',
    'да',
    'давай',
    'давать',
    'давно',
    'даже',
    'далее',
    'далеко',
    'дальше',
    'данный',
    'два',
    'двадцатый',
    'двадцать',
    'дважды',
    'двенадцать',
    'двести',
    'двое',
    'девяносто',
    'девяностый',
    'девятнадцатый',
    'девятый',
    'девять',
    'девятьсот',
    'действительно',
    'делать',
    'день',
    'десятый',
    'десять',
    'дешеветь',
    'дёшево',
    'для',
    'до',
    'добираться',
    'довольно',
    'догадываться',
    'долго',
    'должно',
    'дома',
    'домой',
    'дорого',
    'дорожать',
    'достаточно',
    'дрожать',
    'другой',
    'дружить',
    'дружно',
    'думать',
    'дышать',
    'е',
    'ё',
    'его',
    'едва',
    'ее',
    'её',
    'ей',
    'еле',
    'ему',
    'если',
    'естественно',
    'есть',
    'еще',
    'ещё',
    'ею',
    'ж',
    'жалеть',
    'жалко',
    'жаль',
    'жарко',
    'же',
    'жевать',
    'желать',
    'жизнь',
    'з',
    'за',
    'завидовать',
    'завтра',
    'заглядывать',
    'заговаривать',
    'загорать',
    'заинтересовать',
    'заинтересоваться',
    'закричать',
    'закуривать',
    'замечать',
    'замуж',
    'замужем',
    'заново',
    'заплакать',
    'запланировать',
    'запоминать',
    'заранее',
    'заслуживать',
    'засмеяться',
    'засыпать',
    'затем',
    'зато',
    'захлёбываться',
    'захотеть',
    'захотеться',
    'зачем',
    'звать',
    'звучать',
    'здесь',
    'здорово',
    'здравствовать',
    'знакомиться',
    'знать',
    'зря',
    'и',
    'ибо',
    'играть',
    'идти',
    'из',
    'из-за',
    'из-под',
    'извинять',
    'излагать',
    'изнутри',
    'изображать',
    'изучать',
    'или',
    'им',
    'именно',
    'иметь',
    'иметься',
    'ими',
    'иначе',
    'иногда',
    'иной',
    'интересовать',
    'интересоваться',
    'исключительно',
    'искренне',
    'итак',
    'их',
    'й',
    'к',
    'каждый',
    'кажется',
    'казаться',
    'как',
    'как-то',
    'каков',
    'какой',
    'какой-нибудь',
    'какой-то',
    'кем',
    'кивать',
    'кипеть',
    'клеить',
    'ко',
    'когда',
    'когда-нибудь',
    'когда-то',
    'кого',
    'колебаться',
    'колыхаться',
    'ком',
    'кому',
    'комья',
    'конечно',
    'кормить',
    'коротко',
    'которая',
    'которого',
    'которое',
    'которой',
    'котором',
    'которому',
    'которою',
    'которую',
    'которые',
    'который',
    'которым',
    'которыми',
    'которых',
    'крайне',
    'красиво',
    'крепко',
    'кроме',
    'кругом',
    'кстати',
    'кто',
    'кто-нибудь',
    'кто-то',
    'куда',
    'куда-то',
    'купаться',
    'курить',
    'л',
    'ладно',
    'легко',
    'лень',
    'лет',
    'летать',
    'ли',
    'либо',
    'лично',
    'лишь',
    'ловить',
    'лучше',
    'любоваться',
    'любой',
    'м',
    'мало',
    'махать',
    'мгновенно',
    'между',
    'менее',
    'меня',
    'мечтать',
    'мимо',
    'мимоходом',
    'мне',
    'многие',
    'много',
    'многое',
    'мной',
    'мною',
    'мог',
    'моги',
    'могите',
    'могла',
    'могли',
    'могло',
    'могу',
    'могут',
    'мое',
    'моё',
    'моего',
    'моей',
    'моем',
    'моём',
    'моему',
    'моею',
    'можем',
    'может',
    'можете',
    'можешь',
    'можно',
    'мои',
    'моим',
    'моими',
    'моих',
    'мой',
    'мол',
    'молиться',
    'молча',
    'моргать',
    'Москва',
    'мочить',
    'мочь',
    'мою',
    'моя',
    'мы',
    'мысленно',
    'мыть',
    'мягко',
    'н',
    'на',
    'наверно',
    'наверное',
    'наверняка',
    'наверх',
    'наверху',
    'навсегда',
    'навстречу',
    'над',
    'надевать',
    'надеяться',
    'надо',
    'надоедать',
    'надолго',
    'назад',
    'наиболее',
    'наконец',
    'налево',
    'наливать',
    'нам',
    'нами',
    'намного',
    'наоборот',
    'направо',
    'напрасно',
    'например',
    'напротив',
    'напрямую',
    'наружу',
    'нас',
    'наса',
    'насколько',
    'насмотреться',
    'настолько',
    'насчёт',
    'научиться',
    'начинать',
    'наш',
    'наша',
    'наше',
    'нашего',
    'нашей',
    'нашем',
    'нашему',
    'нашею',
    'наши',
    'нашим',
    'нашими',
    'наших',
    'нашу',
    'невесть',
    'него',
    'негромко',
    'недавно',
    'недалеко',
    'недолго',
    'нее',
    'неё',
    'независимо',
    'неизвестно',
    'ней',
    'некий',
    'некогда',
    'некоторый',
    'некуда',
    'нелегко',
    'нельзя',
    'нем',
    'нём',
    'немало',
    'немедленно',
    'немного',
    'немножко',
    'нему',
    'ненавидеть',
    'ненадолго',
    'необходимо',
    'неоднократно',
    'неожиданно',
    'неплохо',
    'неподалёку',
    'непременно',
    'неприятно',
    'нередко',
    'несколько',
    'несмотря',
    'несомненно',
    'неудобно',
    'неужели',
    'нечего',
    'нечто',
    'нею',
    'ни',
    'нигде',
    'ниже',
    'низко',
    'никак',
    'никакой',
    'никогда',
    'никто',
    'никуда',
    'ним',
    'ними',
    'нисколько',
    'них',
    'ничего',
    'ничто',
    'но',
    'нормально',
    'нравиться',
    'ну',
    'нужно',
    'ныне',
    'о',
    'об',
    'оба',
    'обедать',
    'обидно',
    'обижаться',
    'обнимать',
    'обниматься',
    'обожать',
    'оборачиваться',
    'обрадоваться',
    'обратно',
    'обсуждать',
    'обучаться',
    'обходиться',
    'объяснять',
    'обычно',
    'обязательно',
    'оглядываться',
    'одевать',
    'один',
    'одинаково',
    'одиннадцать',
    'одна',
    'однажды',
    'однако',
    'одни',
    'одним',
    'одними',
    'одних',
    'одно',
    'одновременно',
    'одного',
    'одной',
    'одном',
    'одному',
    'одною',
    'одну',
    'ой',
    'оказываться',
    'около',
    'окончательно',
    'он',
    'она',
    'оне',
    'они',
    'оно',
    'опять',
    'орать',
    'освещать',
    'основываться',
    'особенно',
    'особо',
    'осознавать',
    'остальной',
    'останавливаться',
    'осторожно',
    'от',
    'откуда',
    'отлично',
    'отнюдь',
    'отсюда',
    'оттуда',
    'отчасти',
    'отчётливо',
    'очень',
    'ощущать',
    'п',
    'первый',
    'перебегать',
    'перед',
    'переживать',
    'перекусывать',
    'пересказывать',
    'переспрашивать',
    'периодически',
    'петь',
    'пешком',
    'писаться',
    'плавать',
    'плакать',
    'плотно',
    'плохо',
    'плыть',
    'плюс',
    'по',
    'по-другому',
    'по-прежнему',
    'по-разному',
    'побеждать',
    'поблагодарить',
    'повезти',
    'поверх',
    'поговорить',
    'под',
    'подниматься',
    'подряд',
    'подумать',
    'подчёркивать',
    'поесть',
    'пожалеть',
    'пожалуй',
    'пожалуйста',
    'позади',
    'поздно',
    'поздравлять',
    'позже',
    'пойти',
    'пока',
    'полно',
    'полностью',
    'полтора',
    'полюбить',
    'помимо',
    'понадобиться',
    'понимать',
    'понравиться',
    'поныне',
    'понятно',
    'поперёк',
    'пополам',
    'посвящать',
    'посередине',
    'поскольку',
    'после',
    'постепенно',
    'постоянно',
    'постучать',
    'потеть',
    'потом',
    'поутру',
    'похоже',
    'поцеловать',
    'почему',
    'почему-то',
    'почитать',
    'почти',
    'поэтому',
    'пояснять',
    'правда',
    'правильно',
    'практически',
    'превосходить',
    'предполагать',
    'прежде',
    'прекрасно',
    'преодолевать',
    'при',
    'прибивать',
    'приблизительно',
    'приветствовать',
    'привыкать',
    'примерно',
    'прислушиваться',
    'присниться',
    'причём',
    'приятно',
    'про',
    'пробовать',
    'проглатывать',
    'произносить',
    'просто',
    'просыпаться',
    'против',
    'протягивать',
    'проходить',
    'прочесть',
    'прочий',
    'прощать',
    'прыгать',
    'прямо',
    'пусть',
    'пыхтеть',
    'пятидесятый',
    'пятнадцатый',
    'пятнадцать',
    'пятый',
    'пять',
    'пятьдесят',
    'пятьсот',
    'р',
    'ради',
    'радовать',
    'радоваться',
    'раз',
    'разбираться',
    'разве',
    'развивать',
    'развиваться',
    'разговаривать',
    'раздаваться',
    'размышлять',
    'разумеется',
    'ранее',
    'рано',
    'раньше',
    'рассказывать',
    'рассуждать',
    'рваться',
    'регулярно',
    'редко',
    'резко',
    'решать',
    'рисовать',
    'ровно',
    'россия',
    'ругать',
    'рядом',
    'с',
    'сам',
    'сама',
    'сами',
    'самим',
    'самими',
    'самих',
    'само',
    'самого',
    'самом',
    'самому',
    'самостоятельно',
    'саму',
    'самый',
    'сбоку',
    'сверкать',
    'сверху',
    'светло',
    'свободно',
    'свое',
    'своё',
    'своего',
    'своей',
    'своем',
    'своём',
    'своему',
    'своею',
    'свои',
    'своим',
    'своими',
    'своих',
    'свой',
    'свою',
    'своя',
    'сделать',
    'сдерживать',
    'себе',
    'себя',
    'сегодня',
    'седьмой',
    'сей',
    'сейчас',
    'семеро',
    'семнадцатый',
    'семнадцать',
    'семь',
    'семьдесят',
    'семьсот',
    'сердиться',
    'серьёзно',
    'сзади',
    'сильно',
    'скажем',
    'сказать',
    'скатываться',
    'скачивать',
    'сквозь',
    'складываться',
    'скольки',
    'сколько',
    'скорее',
    'скоро',
    'скучать',
    'слабо',
    'сладко',
    'слева',
    'слегка',
    'следовательно',
    'слишком',
    'словно',
    'сложно',
    'случайно',
    'слышать',
    'слышаться',
    'слышно',
    'смешно',
    'смеяться',
    'смотреть',
    'смочь',
    'снаружи',
    'сначала',
    'снизу',
    'сниться',
    'снова',
    'со',
    'собой',
    'собою',
    'собственно',
    'совершенно',
    'советовать',
    'совсем',
    'согласно',
    'сомневаться',
    'сорок',
    'сороковой',
    'сотый',
    'социально',
    'спасибо',
    'спать',
    'специально',
    'спокойно',
    'справа',
    'справляться',
    'спрашивать',
    'спустя',
    'сразу',
    'среди',
    'стараться',
    'сто',
    'столь',
    'столько',
    'стоп',
    'страдать',
    'странно',
    'стрелять',
    'стремительно',
    'стремиться',
    'строго',
    'стыдно',
    'суметь',
    'сухо',
    'сушить',
    'существовать',
    'счастливо',
    'считать',
    'съесть',
    'сюда',
    'т',
    'та',
    'так',
    'такая',
    'также',
    'такие',
    'таким',
    'такими',
    'таких',
    'таков',
    'таковой',
    'такого',
    'такое',
    'такой',
    'таком',
    'такому',
    'такою',
    'такую',
    'там',
    'танцевать',
    'таскать',
    'твёрдо',
    'твой',
    'те',
    'тебе',
    'тебя',
    'тем',
    'теми',
    'темно',
    'теперь',
    'терпеть',
    'теряться',
    'тесно',
    'тех',
    'течь',
    'тихо',
    'то',
    'тобой',
    'тобою',
    'тогда',
    'того',
    'тоже',
    'той',
    'только',
    'том',
    'томах',
    'тому',
    'тот',
    'точить',
    'точно',
    'тою',
    'традиционно',
    'тревожиться',
    'третий',
    'три',
    'тридцать',
    'трижды',
    'тринадцатый',
    'тринадцать',
    'триста',
    'трое',
    'трудно',
    'ту',
    'туда',
    'тут',
    'тщательно',
    'ты',
    'тяжело',
    'тянуться',
    'у',
    'убеждать',
    'убеждаться',
    'убивать',
    'уважать',
    'уверенно',
    'уверять',
    'увлекаться',
    'увы',
    'угодно',
    'удаваться',
    'удивлять',
    'ужасно',
    'уже',
    'ужинать',
    'украшать',
    'улыбаться',
    'уметь',
    'умножать',
    'умываться',
    'упасть',
    'упоминать',
    'упорно',
    'ура',
    'условно',
    'услышать',
    'успешно',
    'успокаивать',
    'успокаиваться',
    'уставать',
    'ухаживать',
    'ф',
    'фактически',
    'физически',
    'х',
    'хвалить',
    'хорошо',
    'хотеть',
    'хотеться',
    'хоть',
    'хотя',
    'ц',
    'целиком',
    'целовать',
    'целоваться',
    'цель',
    'ценить',
    'цитировать',
    'ч',
    'час',
    'частично',
    'часто',
    'чего',
    'чей',
    'человек',
    'чем',
    'чём',
    'чему',
    'через',
    'честно',
    'четверо',
    'четвёртый',
    'четыре',
    'четырнадцатый',
    'четырнадцать',
    'чисто',
    'читаться',
    'чрезвычайно',
    'что',
    'что-либо',
    'что-нибудь',
    'что-то',
    'чтобы',
    'чувствоваться',
    'чудесно',
    'чуть',
    'чуть-чуть',
    'ш',
    'шагать',
    'шептать',
    'шестнадцатый',
    'шестнадцать',
    'шестой',
    'шесть',
    'шестьдесят',
    'шестьсот',
    'шибко',
    'широко',
    'шить',
    'шляться',
    'шутить',
    'щ',
    'щекотать',
    'ъ',
    'ы',
    'ь',
    'э',
    'эта',
    'эти',
    'этим',
    'этими',
    'этих',
    'это',
    'этого',
    'этой',
    'этом',
    'этому',
    'этот',
    'этою',
    'эту',
    'ю',
    'я',
    'являться',
    'язык',
    'якобы',
    'ярко',
    'ясно',
]
