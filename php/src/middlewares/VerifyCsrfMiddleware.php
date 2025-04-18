<?php

namespace src\middlewares;

use src\core\Request;
use src\core\Response;
use src\middlewares\Middleware;
use src\utils\UserSession;

class VerifyCsrfMiddleware extends Middleware
{
    public function handle(Request $req, Response $res): void
    {
        if (in_array($req->getMethod(), ['POST'])) {
            $csrfToken = $_POST['csrf_token'] ?? ($_GET['csrf_token'] ?? '');
            if (!UserSession::verifyCsrfToken($csrfToken)) {
                $res->renderError([
                    'statusCode' => 403,
                    'message' => 'Forbidden: Invalid CSRF token',
                ]);
                exit;
            }
        }
    }
}
