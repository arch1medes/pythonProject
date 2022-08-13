from flask import Blueprint,jsonify


from posts.dao.comm.dao import Comment DAO
from posts.dao.post.dao import PostDAO
from posts.dao.comm import Comment
from posts.dao.post import Post


from config import DATA_PATH_POSTS,DATA_PATH_COMMENTS


#создаем блупринт
bp_api = Blueprint("bp_api",__name__)

#создаем обьекты доступа к данным
post.dao = PostDAO(DATA_PATH_POSTS)
comm.dao = CommantDaoDAO(DATA_PATH_COMMENTS)


api_logger= logging.getLogger("api_logger")


@bp_api.route('/posts/')
def api_posts_all():
    """эндпоинт для всех постов"""
    all_posts: list[Post] = post.dao.get_all()
    all_posts_as_dicts: list[dict] = [post.as_dict() for post in all_posts]
    api_logger.debug("Запрошены все посты")

    return jsonify(all_posts_as_dicts),200

@bp_api.route('/posts/<int:pk>/')
def api_posts_single(pk: int):
    post: Post|None = post.dao.get_by_pk(pk)

    if post is None:
        api_logger.debug(f"Обращение к несуществующему посту {pk}")
        abort(404)

    api_logger.debug(f"Запрошен пост {pk}")

    return jsonify(post.as_dict()),200

@bp_api.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка {error}")
    return jsonify({"error": str(error)}),404

@bp_api.route('/')
def api_posts_hi():...