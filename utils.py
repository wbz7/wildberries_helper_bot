import parser


def get_thing_sizes(block_sizes):
    sizes = {}
    for block in block_sizes:
        size = str(block).split('\n')[2]
        s_value = size.replace('<span>', '').replace('</span>', '')
        # на случай если размеры у товара не предусмотрены
        if s_value == '0':
            return
        # делаем буквы в нижнем регистре, так же сделаем с
        # введенными пользователем, чтоб не зависеть от регистра
        value = ''
        for i in s_value:
            if i.isalpha():
                i = i.lower()
            value += i
        flag = True
        if 'disabled' in str(block):
            flag = False
        sizes[value] = flag
    return sizes


def get_text_with_items(items):
    """ Преобразуем товары исходя из информации о них в текстовые сообщения
        Возвращаем список этих сообщений
    """
    items_text = []
    for item_id, article, item_size, item_name, url, existence, user_price in items:
        if existence:
            # размеры могут иметь буквенное обозначение, поэтому поле в БД TEXT
            # Приходится отсеивать товары без размера, сравнивая со строкой
            if item_size != '0':
                items_text.append(
                    "*Отслеживание цены:*\n"
                    f"[{item_name}]({url})\n"
                    f"Артикул: {article}\n"
                    f"Размер: {item_size}\n"
                    f"Ожидаемая цена: {user_price}\n"
                    f"*ID* товара: {item_id}\n"
                )
                continue
            items_text.append(
                "*Отслеживание цены:*\n"
                f"[{item_name}]({url})\n"
                f"Артикул: {article}\n"
                f"Ожидаемая цена: {user_price}\n"
                f"*ID* товара: {item_id}\n"
            )
            continue
        # размеры могут иметь буквенное обозначение, поэтому поле в БД TEXT
        # Приходится отсеивать товары без размера, сравнивая со строкой
        if item_size != '0':
            items_text.append(
                "*Отслеживание появления:*\n"
                f"[{item_name}]({url})\n"
                f"Артикул: {article}\n"
                f"Размер: {item_size}\n"
                f"*ID* товара: {item_id}\n"
            )
            continue
        items_text.append(
            "*Отслеживание появления:*\n"
            f"[{item_name}]({url})\n"
            f"Артикул: {article}\n"
            f"*ID* товара: {item_id}\n"
        )
        continue
    return items_text


def get_price_status(items):
    discounted_goods = []
    for item_id, profile, article, item_size, item_name, url, user_price in items:
        price = parser.get_price(article)
        sizes = parser.get_sizes(article)
        template_good = (
            profile,
            item_id,
            f"*Цена достигла ожидаемой*\n"
            f"[{item_name}]({url})"
            f"Артикул: {article}\n"
            f"Ожидаемая: {user_price}\n"
            f"Настоящая: {price}\n"
        )
        template_bad = (
            profile,
            item_id,
            f"*Товар пропал из продажи*\n"
            f"[{item_name}]({url})\n"
            f"Артикул: {article}\n"
        )
        if not price:
            discounted_goods.append(template_bad)
            continue
        if sizes and sizes[item_size]:
            if price <= user_price:
                discounted_goods.append(template_good)
                continue
        if sizes and not sizes[item_size]:
            discounted_goods.append(template_bad)
            continue
        if price <= user_price:
            discounted_goods.append(template_good)
            continue
    return discounted_goods


def get_appeared_goods(items):
    """ Принимает в качестве аргумента товары, появление которых
        отслеживается, проверяет их статус и возвращает список
        кортежей (user_id, item_id, text) появившихся
    """
    appered_goods = []
    for item_id, profile, article, item_size, item_name, url, user_price in items:
        price = parser.get_price(article)
        sizes = parser.get_sizes(article)
        template = (
            profile,
            item_id,
            "*Товар появился в продаже*\n"
            f"[{item_name}]({url})\n"
            f"Артикул: {article}\n"
            f"Цена: {price}"
        )
        if not price:
            continue
        if not sizes:
            appered_goods.append(template)
            continue
        if sizes and sizes[item_size]:
            appered_goods.append(template)
            continue
    return appered_goods
