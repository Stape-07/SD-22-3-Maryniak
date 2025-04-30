from articles_manager import add_article, delete_article, view_articles, close_connection

print("📚 Усі статті:")
view_articles()

print("🗑️ Видаляємо статтю з ID = 2")
delete_article(2)

print("\n📚 Після видалення:")
view_articles()

close_connection()
