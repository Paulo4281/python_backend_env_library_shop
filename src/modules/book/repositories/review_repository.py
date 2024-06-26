from src.modules.book.dtos.review_dto import ReviewDTO, ReviewResponseDTO, ReviewUpdateDTO
from src.modules.book.entities.review import Review
from src.modules.book.entities.book import Book
from src.modules.user.entities.user import User
from src.database.database_config import session
from sqlalchemy.orm import joinedload
from uuid import uuid4
from datetime import datetime
from typing import List

class ReviewRepository:
    @staticmethod
    def save(data: ReviewDTO) -> ReviewResponseDTO:
        try:
            with session.begin():
                review = Review(
                    id_ = uuid4(),
                    rate = data["rate"],
                    review = data["review"],
                    book_id = data["book_id"],
                    user_id = data["user_id"],
                    created_at = datetime.now()
                )

                session.add(review)
            return review.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find() -> List[ReviewResponseDTO]:
        try:
            with session.begin():
                reviews = session.query(Review, Book, User).join(Book).join(User).options(joinedload(Review.book), joinedload(Review.user))

                reviews_list = []

                for review, book, user in reviews:
                    review_dict = review.to_dict()
                    review_dict["book"] = book.to_dict()
                    review_dict["user"] = user.to_dict()
                    reviews_list.append(review.to_dict())

            return reviews_list
        except Exception as e:
            print(str(e))
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_id(id_: str) -> ReviewResponseDTO:
        try:
            with session.begin():
                review = session.query(Review).filter(Review.id_ == id_).first()

            return review.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: ReviewUpdateDTO) -> None:
        try:
            with session.begin():
                session.query(Review).filter(Review.id_ == id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(Review).filter(Review.id_ == id_).delete()
        except:
            session.rollback()
        finally:
            session.close()