import com.sun.net.httpserver.{HttpExchange, HttpHandler}

case class DefaultHandler() extends HttpHandler {
  def handle(httpExchange: HttpExchange): Unit = {
    httpExchange.sendResponseHeaders(404, -1)
    httpExchange.getResponseBody.close()
  }
}
